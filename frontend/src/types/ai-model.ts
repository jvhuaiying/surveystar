export type CreateAiModelRequestSchemas = {
  name: string;
  api_key: string;
  base_url: string;
  is_active: boolean;
  model_type: string;
  provider_id: string;
};

export type UpdateAiModelRequestSchemas = {
  name: string;
  api_key: string;
  base_url: string;
  is_active: boolean;
  model_type: string;
  provider_id: string;
};

export type AiModelTestStatus = "untested" | "success" | "failed";

export type GetAiModelResponseSchemas = {
  id: string;
  name: string;
  api_key: string;
  base_url: string;
  is_active: boolean;
  model_type: string;
  test_status: AiModelTestStatus;
  provider_id: string;
  created_at: string;
  updated_at: string;
};

export type AiModelDialogMode = "create" | "edit";

export type MessageResponseSchemas = {
  detail: string;
};
