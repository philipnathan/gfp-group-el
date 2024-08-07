'use client'

import { HoverCard, HoverCardContent, HoverCardTrigger } from "@/components/ui/hover-card"

export default function ChatPage() {
  return (
    <div className="p-10">
      <HoverCard>
        <HoverCardTrigger>
          <button className="bg-blue-500 text-white px-4 py-2 rounded">
            Hover me
          </button>
        </HoverCardTrigger>
        <HoverCardContent>
          The React Framework – created and maintained by @vercel.
        </HoverCardContent>
      </HoverCard>
    </div>
  );
}
