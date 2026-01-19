import { Bell, Search, MessageSquare } from 'lucide-react';
import { ThemeToggle } from '../theme/ThemeToggle';
import { cn } from '../../lib/utils';

interface HeaderProps {
  className?: string;
}

export function Header({ className }: HeaderProps) {
  return (
    <header
      className={cn(
        'fixed top-0 right-0 left-72 z-30 h-16 theme-bg border-b theme-border',
        'flex items-center justify-between px-6',
        className
      )}
    >
      {/* Search */}
      <div className="flex-1 max-w-xl">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 theme-text-muted" />
          <input
            type="text"
            placeholder="Search KPIs, metrics, insights..."
            className="w-full h-10 pl-10 pr-4 rounded-xl theme-card-bg border theme-border
              focus:outline-none focus:ring-2 focus:ring-alpha-500 focus:border-transparent
              theme-text placeholder:theme-text-muted transition-all duration-200"
          />
        </div>
      </div>

      {/* Right side actions */}
      <div className="flex items-center gap-2">
        {/* AI Strategist Button */}
        <button
          className="flex items-center gap-2 px-4 py-2 rounded-xl
            bg-alpha-600 text-white hover:bg-alpha-500
            transition-all duration-200 hover:scale-105 active:scale-95"
        >
          <MessageSquare className="w-4 h-4" />
          <span className="text-sm font-medium">AI Strategist</span>
        </button>

        {/* Notifications */}
        <button
          className="relative p-2 rounded-lg theme-text-muted hover:theme-card-bg transition-all duration-200"
          aria-label="Notifications"
        >
          <Bell className="w-5 h-5" />
          <span className="absolute top-1 right-1 w-2 h-2 bg-gamma-500 rounded-full" />
        </button>

        {/* Theme Toggle */}
        <ThemeToggle />

        {/* User Avatar */}
        <button className="w-9 h-9 rounded-full bg-gradient-to-br from-alpha-400 to-alpha-600 flex items-center justify-center text-white font-medium text-sm">
          JD
        </button>
      </div>
    </header>
  );
}
