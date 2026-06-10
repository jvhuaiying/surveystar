export type CreateAiProviderRequestSchemas = {
  name: string;
  is_active: boolean;
};

export type UpdateAiProviderRequestSchemas = {
  name: string;
  is_active: boolean;
};

export type GetAiProviderResponseSchemas = {
  id: string;
  name: string;
  is_active: boolean;
  created_at: string;
  updated_at: string;
};

export type AiProviderDialogMode = "create" | "edit";

export type MessageResponseSchemas = {
  detail: string;
};
