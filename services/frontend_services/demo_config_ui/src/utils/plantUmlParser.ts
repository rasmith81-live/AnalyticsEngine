/**
 * PlantUML Parser Utility
 * Extracts entities and relationships from PlantUML schema definitions
 */

export interface Entity {
  name: string;
  type: 'class' | 'entity';
}

export interface Relationship {
  from: string;
  to: string;
  type: string; // e.g., "1..*", "0..1", "1", "*"
  label?: string;
  direction: 'left' | 'right' | 'both';
}

export interface ParsedSchema {
  entities: Entity[];
  relationships: Relationship[];
}

/**
 * Parse PlantUML schema definition to extract entities and relationships
 */
export function parsePlantUML(schemaDefinition: string): ParsedSchema {
  if (!schemaDefinition) {
    return { entities: [], relationships: [] };
  }

  const entities = new Set<string>();
  const relationships: Relationship[] = [];

  // Split into lines and clean
  const lines = schemaDefinition
    .split('\n')
    .map(line => line.trim())
    .filter(line => line && !line.startsWith('@') && !line.startsWith("'"));

  // Relationship patterns
  // Format: EntityA "cardinality" -- "cardinality" EntityB : label
  // Examples:
  // - Account "1" -- "0..*" Lead : generates >
  // - SalesTeam "1..*" -- "0..*" Account : manages >
  const relationshipPattern = /^(\w+)\s+"([^"]+)"\s+(--|-\|>|<\|-|<\|>)\s+"([^"]+)"\s+(\w+)(?:\s*:\s*(.+))?$/;

  for (const line of lines) {
    const match = line.match(relationshipPattern);
    if (match) {
      const [, fromEntity, fromCard, arrow, toCard, toEntity, label] = match;
      
      // Add entities
      entities.add(fromEntity);
      entities.add(toEntity);

      // Determine direction based on arrow
      let direction: 'left' | 'right' | 'both' = 'both';
      if (arrow.includes('>') && !arrow.includes('<')) {
        direction = 'right';
      } else if (arrow.includes('<') && !arrow.includes('>')) {
        direction = 'left';
      }

      // Add relationship
      relationships.push({
        from: fromEntity,
        to: toEntity,
        type: `${fromCard} to ${toCard}`,
        label: label?.trim().replace(/[<>]/g, ''),
        direction,
      });
    }
  }

  return {
    entities: Array.from(entities).map(name => ({ name, type: 'entity' as const })),
    relationships,
  };
}

/**
 * Get relationship cardinality display text
 */
export function getCardinalityText(type: string): string {
  const cardMap: Record<string, string> = {
    '1 to 1': 'One to One',
    '1 to 0..1': 'One to Zero or One',
    '1 to 0..*': 'One to Many',
    '1 to *': 'One to Many',
    '1..* to 0..*': 'Many to Many',
    '0..1 to 0..1': 'Zero or One to Zero or One',
    '* to *': 'Many to Many',
  };
  return cardMap[type] || type;
}

/**
 * Filter relationships by entity
 */
export function filterRelationshipsByEntity(
  relationships: Relationship[],
  entityName: string
): Relationship[] {
  return relationships.filter(
    rel => rel.from === entityName || rel.to === entityName
  );
}

/**
 * Get connected entities for a given entity
 */
export function getConnectedEntities(
  relationships: Relationship[],
  entityName: string
): string[] {
  const connected = new Set<string>();
  
  relationships.forEach(rel => {
    if (rel.from === entityName) {
      connected.add(rel.to);
    }
    if (rel.to === entityName) {
      connected.add(rel.from);
    }
  });

  return Array.from(connected);
}

/**
 * Calculate graph statistics
 */
export function getGraphStats(schema: ParsedSchema) {
  const entityCount = schema.entities.length;
  const relationshipCount = schema.relationships.length;
  
  // Calculate degree (connections) for each entity
  const degrees = new Map<string, number>();
  schema.entities.forEach(entity => degrees.set(entity.name, 0));
  
  schema.relationships.forEach(rel => {
    degrees.set(rel.from, (degrees.get(rel.from) || 0) + 1);
    degrees.set(rel.to, (degrees.get(rel.to) || 0) + 1);
  });

  const maxDegree = Math.max(...Array.from(degrees.values()));
  const avgDegree = Array.from(degrees.values()).reduce((a, b) => a + b, 0) / entityCount;

  return {
    entityCount,
    relationshipCount,
    maxDegree,
    avgDegree: Math.round(avgDegree * 10) / 10,
    mostConnected: Array.from(degrees.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(([name, degree]) => ({ name, degree })),
  };
}
