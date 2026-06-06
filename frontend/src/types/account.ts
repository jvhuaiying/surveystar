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
