export type CreateSystemPromptRequestSchemas = {
  content: string;
  is_active: boolean;
  account_id: string;
};

export type GetSystemPromptResponseSchemas = {
  id: string;
  content: string;
  is_active: boolean;
  account_id: string;
  account_nickname: string;
};

export type MessageResponseSchemas = {
  detail: string;
};
