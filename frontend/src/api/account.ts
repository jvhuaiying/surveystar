import request from "@/utils/request";
import type {
  GetAccountListResponseSchemas,
  SigninRequestSchemas,
  SigninResponseSchemas,
} from "@/types/account";

export const signin = (data: SigninRequestSchemas): Promise<SigninResponseSchemas> => {
  return request
    .post("/account/signin", data)
    .then((res) => res.data)
    .catch((err) => {
      throw err;
    });
};

export const getAccountList = (): Promise<GetAccountListResponseSchemas[]> => {
  return request
    .get("/account/")
    .then((res) => res.data)
    .catch((err) => {
      throw err;
    });
};
