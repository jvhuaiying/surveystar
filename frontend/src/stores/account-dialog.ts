import { ref } from "vue";
import { defineStore } from "pinia";
import type { AccountDialogMode } from "@/types/account";

export const useAccountDialogStore = defineStore("accountDialog", () => {
  const visible = ref(false);
  const mode = ref<AccountDialogMode>("create");
  const currentId = ref<string | null>(null);

  const open = (dialogMode: AccountDialogMode, currentIdValue: string | null) => {
    mode.value = dialogMode;
    currentId.value = currentIdValue;
    visible.value = true;
  };

  const close = () => {
    visible.value = false;
    mode.value = "create";
    currentId.value = null;
  };

  return { visible, mode, currentId, open, close };
});
