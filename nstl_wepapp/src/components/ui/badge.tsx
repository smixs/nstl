import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const badgeVariants = cva(
  "inline-flex items-center rounded-full px-3 py-1.5 text-xs font-medium transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-offset-2",
  {
    variants: {
      variant: {
        default:
          "bg-primary-soft text-primary hover:shadow-md",
        secondary:
          "bg-secondary-soft text-secondary hover:shadow-md",
        destructive:
          "bg-secondary-soft text-secondary hover:shadow-md",
        outline: "border border-gray-300 bg-transparent hover:bg-gray-50",
        success:
          "bg-success-soft text-success hover:shadow-md",
        gradient:
          "bg-gradient-to-r from-[var(--color-primary)] to-[var(--color-secondary)] text-gray-700 hover:shadow-md",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return (
    <div className={cn(badgeVariants({ variant }), className)} {...props} />
  )
}

export { Badge, badgeVariants }