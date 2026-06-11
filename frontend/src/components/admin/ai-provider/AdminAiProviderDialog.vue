<script setup lang="ts">
import { useTemplateRef } from "vue";
import { useAiProviderDialogStore } from "@/stores/ai-provider-dialog";
import AdminAiProviderEditForm from "@/components/admin/ai-provider/AdminAiProviderEditForm.vue";
import AdminAiProviderForm from "@/components/admin/ai-provider/AdminAiProviderForm.vue";

const dialogStore = useAiProviderDialogStore();
const dialogRef = useTemplateRef<HTMLDialogElement>("dialogRef");

dialogStore.$subscribe((_mutation, state) => {
  if (state.visible) {
    dialogRef.value?.showModal();
  } else {
    dialogRef.value?.close();
  }
});

const onClose = () => {
  if (dialogStore.visible) {
    dialogStore.close();
  }
};
</script>

<template>
  <dialog
    ref="dialogRef"
    @close="onClose"
    class="m-auto p-6 w-96 bg-white rounded-lg shadow-md border border-gray-200"
  >
    <div class="w-full flex flex-col justify-center items-center gap-y-4">
      <h1 class="text-2xl font-[AlimamaDongFangDaKai] text-center">
        {{ dialogStore.mode === "create" ? "新增供应商" : "编辑供应商" }}
      </h1>
      <AdminAiProviderForm model="dialog" v-show="dialogStore.mode === 'create'" />
      <AdminAiProviderEditForm v-show="dialogStore.mode === 'edit'" />
    </div>
  </dialog>
</template>
