# Shadcn/ui Component Reference

Quick reference for commonly used Shadcn components in prototypes.

## Table of Contents
- [Installation](#installation)
- [Core Components](#core-components)
- [Layout Components](#layout-components)
- [Advanced Components](#advanced-components)
- [Form Validation](#form-validation)
- [Icons](#icons)
- [Common Patterns](#common-patterns)
- [Resources](#resources)

## Installation

Install components as needed:

```bash
npx shadcn@latest add [component-name]
```

## Core Components

### Button

**Install**: `npx shadcn@latest add button`

```tsx
import { Button } from "@/components/ui/button"

<Button>Click me</Button>
<Button variant="outline">Secondary</Button>
<Button variant="destructive">Delete</Button>
<Button variant="ghost">Subtle</Button>
<Button size="sm">Small</Button>
<Button size="lg">Large</Button>
```

**Variants**: default, destructive, outline, secondary, ghost, link
**Sizes**: default, sm, lg, icon

### Card

**Install**: `npx shadcn@latest add card`

```tsx
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card"

<Card>
  <CardHeader>
    <CardTitle>Title</CardTitle>
    <CardDescription>Description</CardDescription>
  </CardHeader>
  <CardContent>
    Content goes here
  </CardContent>
  <CardFooter>
    Footer actions
  </CardFooter>
</Card>
```

### Input

**Install**: `npx shadcn@latest add input`

```tsx
import { Input } from "@/components/ui/input"

<Input type="text" placeholder="Enter text" />
<Input type="email" placeholder="Email" />
<Input type="password" placeholder="Password" />
```

### Form

**Install**: `npx shadcn@latest add form input label`

```tsx
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { useForm } from "react-hook-form"

const form = useForm()

<Form {...form}>
  <form onSubmit={form.handleSubmit(onSubmit)}>
    <FormField
      control={form.control}
      name="username"
      render={({ field }) => (
        <FormItem>
          <FormLabel>Username</FormLabel>
          <FormControl>
            <Input placeholder="Enter username" {...field} />
          </FormControl>
          <FormMessage />
        </FormItem>
      )}
    />
  </form>
</Form>
```

### Dialog

**Install**: `npx shadcn@latest add dialog`

```tsx
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"

<Dialog>
  <DialogTrigger asChild>
    <Button>Open Dialog</Button>
  </DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Are you sure?</DialogTitle>
      <DialogDescription>
        This action cannot be undone.
      </DialogDescription>
    </DialogHeader>
  </DialogContent>
</Dialog>
```

### Select / Dropdown

**Install**: `npx shadcn@latest add select`

```tsx
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

<Select>
  <SelectTrigger className="w-[180px]">
    <SelectValue placeholder="Select option" />
  </SelectTrigger>
  <SelectContent>
    <SelectItem value="option1">Option 1</SelectItem>
    <SelectItem value="option2">Option 2</SelectItem>
    <SelectItem value="option3">Option 3</SelectItem>
  </SelectContent>
</Select>
```

### Table

**Install**: `npx shadcn@latest add table`

```tsx
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"

<Table>
  <TableHeader>
    <TableRow>
      <TableHead>Name</TableHead>
      <TableHead>Email</TableHead>
      <TableHead>Status</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>
    <TableRow>
      <TableCell>John Doe</TableCell>
      <TableCell>john@example.com</TableCell>
      <TableCell>Active</TableCell>
    </TableRow>
  </TableBody>
</Table>
```

### Tabs

**Install**: `npx shadcn@latest add tabs`

```tsx
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

<Tabs defaultValue="tab1">
  <TabsList>
    <TabsTrigger value="tab1">Tab 1</TabsTrigger>
    <TabsTrigger value="tab2">Tab 2</TabsTrigger>
  </TabsList>
  <TabsContent value="tab1">Content 1</TabsContent>
  <TabsContent value="tab2">Content 2</TabsContent>
</Tabs>
```

### Toast

**Install**: `npx shadcn@latest add toast`

```tsx
import { useToast } from "@/hooks/use-toast"
import { Toaster } from "@/components/ui/toaster"

function Component() {
  const { toast } = useToast()

  return (
    <>
      <Button onClick={() => toast({ title: "Success!", description: "Action completed" })}>
        Show Toast
      </Button>
      <Toaster />
    </>
  )
}
```

### Checkbox

**Install**: `npx shadcn@latest add checkbox`

```tsx
import { Checkbox } from "@/components/ui/checkbox"

<Checkbox id="terms" />
<label htmlFor="terms">Accept terms</label>
```

### Radio Group

**Install**: `npx shadcn@latest add radio-group`

```tsx
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"

<RadioGroup defaultValue="option1">
  <div className="flex items-center space-x-2">
    <RadioGroupItem value="option1" id="option1" />
    <label htmlFor="option1">Option 1</label>
  </div>
  <div className="flex items-center space-x-2">
    <RadioGroupItem value="option2" id="option2" />
    <label htmlFor="option2">Option 2</label>
  </div>
</RadioGroup>
```

### Badge

**Install**: `npx shadcn@latest add badge`

```tsx
import { Badge } from "@/components/ui/badge"

<Badge>Default</Badge>
<Badge variant="secondary">Secondary</Badge>
<Badge variant="destructive">Error</Badge>
<Badge variant="outline">Outline</Badge>
```

### Avatar

**Install**: `npx shadcn@latest add avatar`

```tsx
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"

<Avatar>
  <AvatarImage src="https://github.com/shadcn.png" />
  <AvatarFallback>CN</AvatarFallback>
</Avatar>
```

## Layout Components

### Separator

**Install**: `npx shadcn@latest add separator`

```tsx
import { Separator } from "@/components/ui/separator"

<Separator />
<Separator orientation="vertical" />
```

### Accordion

**Install**: `npx shadcn@latest add accordion`

```tsx
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion"

<Accordion type="single" collapsible>
  <AccordionItem value="item-1">
    <AccordionTrigger>Section 1</AccordionTrigger>
    <AccordionContent>Content for section 1</AccordionContent>
  </AccordionItem>
  <AccordionItem value="item-2">
    <AccordionTrigger>Section 2</AccordionTrigger>
    <AccordionContent>Content for section 2</AccordionContent>
  </AccordionItem>
</Accordion>
```

## Advanced Components

### Command

**Install**: `npx shadcn@latest add command`

Great for search/command palettes.

```tsx
import { Command, CommandInput, CommandList, CommandEmpty, CommandGroup, CommandItem } from "@/components/ui/command"

<Command>
  <CommandInput placeholder="Search..." />
  <CommandList>
    <CommandEmpty>No results found.</CommandEmpty>
    <CommandGroup heading="Suggestions">
      <CommandItem>Calendar</CommandItem>
      <CommandItem>Search Emoji</CommandItem>
      <CommandItem>Calculator</CommandItem>
    </CommandGroup>
  </CommandList>
</Command>
```

### Popover

**Install**: `npx shadcn@latest add popover`

```tsx
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"

<Popover>
  <PopoverTrigger asChild>
    <Button variant="outline">Open</Button>
  </PopoverTrigger>
  <PopoverContent>
    Place content here.
  </PopoverContent>
</Popover>
```

### Calendar

**Install**: `npx shadcn@latest add calendar`

```tsx
import { Calendar } from "@/components/ui/calendar"
import { useState } from "react"

const [date, setDate] = useState<Date | undefined>(new Date())

<Calendar mode="single" selected={date} onSelect={setDate} />
```

### Data Table

**Install**: `npx shadcn@latest add table`

See https://ui.shadcn.com/docs/components/data-table for full implementation guide.

## Form Validation

For forms with validation, use react-hook-form and zod:

```bash
npm install react-hook-form zod @hookform/resolvers
npx shadcn@latest add form
```

```tsx
import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import * as z from "zod"

const formSchema = z.object({
  username: z.string().min(2).max(50),
  email: z.string().email(),
})

const form = useForm<z.infer<typeof formSchema>>({
  resolver: zodResolver(formSchema),
  defaultValues: { username: "", email: "" },
})

function onSubmit(values: z.infer<typeof formSchema>) {
  console.log(values)
}
```

## Icons

Shadcn uses Lucide icons:

```bash
npm install lucide-react
```

```tsx
import { Check, X, ChevronRight, Menu, Search } from "lucide-react"

<Check className="h-4 w-4" />
<Button><Menu className="mr-2 h-4 w-4" /> Menu</Button>
```

Browse icons: https://lucide.dev/icons/

## Common Patterns

### Loading States

```tsx
import { Button } from "@/components/ui/button"
import { Loader2 } from "lucide-react"

<Button disabled>
  <Loader2 className="mr-2 h-4 w-4 animate-spin" />
  Please wait
</Button>
```

### Empty States

```tsx
<div className="flex flex-col items-center justify-center p-8 text-center">
  <p className="text-muted-foreground">No items found</p>
  <Button className="mt-4">Add New Item</Button>
</div>
```

### Error States

```tsx
import { AlertCircle } from "lucide-react"

<div className="rounded-md bg-destructive/15 p-4">
  <div className="flex">
    <AlertCircle className="h-4 w-4 text-destructive" />
    <p className="ml-2 text-sm text-destructive">Error message here</p>
  </div>
</div>
```

## Resources

- Component Docs: https://ui.shadcn.com/docs/components
- Examples: https://ui.shadcn.com/examples
- Themes: https://ui.shadcn.com/themes
- GitHub: https://github.com/shadcn/ui
