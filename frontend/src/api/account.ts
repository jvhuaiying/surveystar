import request from "@/utils/request";
import type { SigninRequestSchemas, SigninResponseSchemas } from "@/types/account";

export const signin = (data: SigninRequestSchemas): Promise<SigninResponseSchemas> => {
  return request
    .post("/account/signin", data)
    .then((res) => res.data)
    .catch((err) => {
      throw err;
    });
};
