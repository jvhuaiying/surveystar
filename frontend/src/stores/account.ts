import { reactive } from "vue";
import { defineStore } from "pinia";
import type { SigninResponseSchemas } from "@/types/account";

export const useAccountStore = defineStore("account", () => {
  const signinInfo = reactive<SigninResponseSchemas>({
    access_token: "",
    id: "",
    nickname: "",
    email: "",
    kind: "user",
    is_active: false,
  });

  const setSigninInfo = (data: SigninResponseSchemas) => {
    Object.assign(signinInfo, data);
  };

  const clearSigninInfo = () => {
    signinInfo.access_token = "";
    signinInfo.id = "";
    signinInfo.nickname = "";
    signinInfo.email = "";
    signinInfo.kind = "user";
    signinInfo.is_active = false;
  };

  return { signinInfo, setSigninInfo, clearSigninInfo };
});
