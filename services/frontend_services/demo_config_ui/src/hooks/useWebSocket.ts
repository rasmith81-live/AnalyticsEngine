import { useEffect, useRef, useState, useCallback } from 'react';

interface WebSocketMessage {
  type: string;
  payload: any;
  correlation_id?: string;
}

interface UseWebSocketOptions {
  url?: string;
  onOpen?: () => void;
  onClose?: () => void;
  onError?: (event: Event) => void;
  reconnectAttempts?: number;
  reconnectInterval?: number;
}

export const useWebSocket = (options: UseWebSocketOptions = {}) => {
  const {
    url = 'ws://127.0.0.1:8090/ws', // Default to local API Gateway
    onOpen,
    onClose,
    onError,
    reconnectAttempts = 5,
    reconnectInterval = 3000,
  } = options;

  const ws = useRef<WebSocket | null>(null);
  const [isConnected, setIsConnected] = useState(false);
  const [lastMessage, setLastMessage] = useState<WebSocketMessage | null>(null);
  const reconnectCount = useRef(0);

  const connect = useCallback(() => {
    try {
      ws.current = new WebSocket(url);

      ws.current.onopen = () => {
        console.log('WebSocket connected');
        setIsConnected(true);
        reconnectCount.current = 0;
        if (onOpen) onOpen();
      };

      ws.current.onclose = () => {
        console.log('WebSocket disconnected');
        setIsConnected(false);
        if (onClose) onClose();

        // Attempt reconnect
        if (reconnectCount.current < reconnectAttempts) {
          reconnectCount.current += 1;
          setTimeout(() => {
            console.log(`Reconnecting... Attempt ${reconnectCount.current}`);
            connect();
          }, reconnectInterval);
        }
      };

      ws.current.onerror = (event) => {
        console.error('WebSocket error:', event);
        if (onError) onError(event);
      };

      ws.current.onmessage = (event) => {
        try {
          const message: WebSocketMessage = JSON.parse(event.data);
          setLastMessage(message);
        } catch (e) {
          console.error('Failed to parse WebSocket message:', event.data);
        }
      };
    } catch (error) {
      console.error('Failed to create WebSocket connection:', error);
    }
  }, [url, onOpen, onClose, onError, reconnectAttempts, reconnectInterval]);

  useEffect(() => {
    connect();

    return () => {
      if (ws.current) {
        ws.current.close();
      }
    };
  }, [connect]);

  const sendMessage = useCallback((type: string, payload: any) => {
    if (ws.current && ws.current.readyState === WebSocket.OPEN) {
      ws.current.send(JSON.stringify({ type, payload }));
    } else {
      console.warn('WebSocket is not connected. Message not sent:', type);
    }
  }, []);

  const subscribe = useCallback((topic: string) => {
    sendMessage('subscribe', { topic });
  }, [sendMessage]);

  const unsubscribe = useCallback((topic: string) => {
    sendMessage('unsubscribe', { topic });
  }, [sendMessage]);

  return {
    isConnected,
    lastMessage,
    sendMessage,
    subscribe,
    unsubscribe,
  };
};
