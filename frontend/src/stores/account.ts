import { ref } from "vue";
import { defineStore } from "pinia";
import type { SigninResponseSchemas } from "@/types/account";

export const useAccountStore = defineStore(
  "account",
  () => {
    const access_token = ref("");
    const id = ref("");
    const nickname = ref("");
    const email = ref("");
    const kind = ref<"admin" | "user">("user");
    const status = ref<"active" | "disabled" | "deleted">("active");

    const setAccountInfo = (data: SigninResponseSchemas) => {
      access_token.value = data.access_token;
      id.value = data.id;
      nickname.value = data.nickname;
      email.value = data.email;
      kind.value = data.kind;
      status.value = data.status;
    };

    const clearAccountInfo = () => {
      access_token.value = "";
      id.value = "";
      nickname.value = "";
      email.value = "";
      kind.value = "user";
      status.value = "active";
    };

    return { access_token, id, nickname, email, kind, status, setAccountInfo, clearAccountInfo };
  },
  {
    persist: {
      storage: localStorage,
      pick: ["access_token", "id", "nickname", "email", "kind", "status"],
    },
  },
);
