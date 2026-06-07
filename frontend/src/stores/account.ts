import { reactive } from "vue";
import { defineStore } from "pinia";
import type { SigninResponseSchemas } from "@/types/account";

export const useAccountStore = defineStore("account", () => {
  const accountInfo = reactive<SigninResponseSchemas>({
    access_token: "",
    id: "",
    nickname: "",
    email: "",
    kind: "user",
    status: "active",
  });

  const setAccountInfo = (data: SigninResponseSchemas) => {
    Object.assign(accountInfo, data);
  };

  const clearAccountInfo = () => {
    accountInfo.access_token = "";
    accountInfo.id = "";
    accountInfo.nickname = "";
    accountInfo.email = "";
    accountInfo.kind = "user";
    accountInfo.status = "active";
  };

  return { accountInfo, setAccountInfo, clearAccountInfo };
});
