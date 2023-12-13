import { FC } from "react";
import { ChatStyleSelector } from "./chat-empty-state/chat-style-selector";

interface Prop {}

export const ChatHeader: FC<Prop> = (props) => {
  return (
    <div className="flex flex-col gap-2">
      <div className="flex gap-2">
        <ChatStyleSelector disable={true} />
      </div>
    </div>
  );
};
