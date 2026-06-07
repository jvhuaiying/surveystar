export type SigninRequestSchemas = {
  email: string;
  password: string;
  kind: "admin" | "user";
  remember: boolean;
};

export type SigninResponseSchemas = {
  access_token: string;
  id: string;
  nickname: string;
  email: string;
  kind: "admin" | "user";
  status: "active" | "disabled" | "deleted";
};

export type CreateAccountRequestSchemas = {
  nickname: string;
  email: string;
  password: string;
  status: "active" | "disabled" | "deleted";
  kind: "admin" | "user";
};

export type MessageResponseSchemas = {
  detail: string;
};

export type GetAccountResponseSchemas = {
  id: string;
  nickname: string;
  email: string;
  status: "active" | "disabled" | "deleted";
  kind: "admin" | "user";
  created_at: string;
  updated_at: string;
};
