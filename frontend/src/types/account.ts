export type AccountStatus = "active" | "disabled";
export type AccountKind = "admin" | "user";

export type SigninRequestSchemas = {
  email: string;
  password: string;
  kind: AccountKind;
  remember: boolean;
};

export type SigninResponseSchemas = {
  access_token: string;
  id: string;
  nickname: string;
  email: string;
  kind: AccountKind;
  status: AccountStatus;
};

export type CreateAccountRequestSchemas = {
  nickname: string;
  email: string;
  password: string;
  status: AccountStatus;
  kind: AccountKind;
};

export type UpdateAccountRequestSchemas = {
  nickname: string;
  email: string;
  status: AccountStatus;
  kind: AccountKind;
};

export type MessageResponseSchemas = {
  detail: string;
};

export type AccountDialogMode = "create" | "edit";

export type GetAccountResponseSchemas = {
  id: string;
  nickname: string;
  email: string;
  status: AccountStatus;
  kind: AccountKind;
  created_at: string;
  updated_at: string;
};
