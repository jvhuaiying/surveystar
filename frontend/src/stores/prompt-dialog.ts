import { ref } from "vue";
import { defineStore } from "pinia";

export const usePromptDialogStore = defineStore("promptDialog", () => {
  const visible = ref(false);
  const mode = ref<"create" | "edit">("create");
  const currentId = ref<string | null>(null);

  const open = (dialogMode: "create" | "edit", currentIdValue: string | null) => {
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
