import { ref } from "vue";
import { defineStore } from "pinia";

export const useAccountDialogStore = defineStore("accountDialog", () => {
  const visible = ref(false);

  const open = () => {
    visible.value = true;
  };

  const close = () => {
    visible.value = false;
  };

  return { visible, open, close };
});
