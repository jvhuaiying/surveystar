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
    is_active: false,
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
    accountInfo.is_active = false;
  };

  return { accountInfo, setAccountInfo, clearAccountInfo };
});
