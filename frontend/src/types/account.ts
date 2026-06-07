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
  is_active: boolean;
};

export type CreateAccountRequestSchemas = {
  nickname: string;
  email: string;
  password: string;
  is_active: boolean;
  kind: "admin" | "user";
};

export type GetAccountResponseSchemas = {
  id: string;
  nickname: string;
  email: string;
  is_active: boolean;
  kind: "admin" | "user";
  created_at: string;
  updated_at: string;
};
