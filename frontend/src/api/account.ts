import type { AxiosError } from "axios";
import request from "@/utils/request";
import type {
  CreateAccountRequestSchemas,
  GetAccountResponseSchemas,
  MessageResponseSchemas,
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

export const createAccount = (data: CreateAccountRequestSchemas): Promise<MessageResponseSchemas> => {
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

export const disableAccount = (id: string): Promise<MessageResponseSchemas> => {
  return request
    .patch(`/account/${id}/disable`)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "禁用账号失败！");
    });
};

export const activateAccount = (id: string): Promise<MessageResponseSchemas> => {
  return request
    .patch(`/account/${id}/activate`)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "激活账号失败！");
    });
};

export const deleteAccount = (id: string): Promise<MessageResponseSchemas> => {
  return request
    .delete(`/account/${id}`)
    .then((res) => res.data)
    .catch((err: AxiosError<{ detail: string }>) => {
      throw new Error(err.response?.data?.detail || "删除账号失败！");
    });
};
