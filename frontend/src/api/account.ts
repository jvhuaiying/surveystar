import type { AxiosError } from "axios";
import request from "@/utils/request";
import type {
  CreateAccountRequestSchemas,
  GetAccountResponseSchemas,
  SigninRequestSchemas,
  SigninResponseSchemas,
} from "@/types/account";

export const signin = (data: SigninRequestSchemas): Promise<SigninResponseSchemas> => {
  return request
    .post("/account/signin", data)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "登录失败！");
    });
};

export const createAccount = (data: CreateAccountRequestSchemas): Promise<GetAccountResponseSchemas> => {
  return request
    .post("/account/", data)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "创建账号失败！");
    });
};

export const getAccountList = (): Promise<GetAccountResponseSchemas[]> => {
  return request
    .get("/account/")
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "获取账号列表失败！");
    });
};
