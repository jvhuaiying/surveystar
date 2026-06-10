import { ref } from "vue";
import { defineStore } from "pinia";
import type { AiProviderDialogMode } from "@/types/ai-model";

export const useAiProviderDialogStore = defineStore("aiProviderDialog", () => {
  const visible = ref(false);
  const mode = ref<AiProviderDialogMode>("create");
  const currentId = ref<string | null>(null);

  const open = (dialogMode: AiProviderDialogMode, currentIdValue: string | null) => {
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
