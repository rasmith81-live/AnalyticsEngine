import { forwardRef, ButtonHTMLAttributes } from 'react';
import { cn } from '../../lib/utils';

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
}

const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = 'primary', size = 'md', children, ...props }, ref) => {
    const baseStyles = `
      inline-flex items-center justify-center rounded-full font-medium
      transition-all duration-300 hover:scale-105 active:scale-95 active:duration-75
      disabled:opacity-50 disabled:pointer-events-none
    `;

    const variants = {
      primary: 'bg-alpha-600 text-white hover:bg-alpha-300',
      secondary: 'bg-alpha-faded-800 text-white hover:bg-alpha-faded-600',
      outline: 'border border-alpha-faded-300 bg-transparent hover:bg-alpha-faded-50 text-[var(--text-primary)]',
      ghost: 'hover:bg-alpha-faded-50 text-[var(--text-primary)]',
    };

    const sizes = {
      sm: 'h-9 px-4 text-sm',
      md: 'h-11 px-6 text-base',
      lg: 'h-12 px-8 text-lg',
    };

    return (
      <button
        ref={ref}
        className={cn(baseStyles, variants[variant], sizes[size], className)}
        {...props}
      >
        {children}
      </button>
    );
  }
);

Button.displayName = 'Button';

export { Button };
