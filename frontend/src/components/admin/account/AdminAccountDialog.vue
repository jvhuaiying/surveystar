<script setup lang="ts">
import { useTemplateRef } from "vue";
import { useAccountDialogStore } from "@/stores/account-dialog";
import AdminAccountForm from "@/components/admin/account/AdminAccountForm.vue";

const dialogStore = useAccountDialogStore();
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
      <h1 class="text-2xl font-[AlimamaDongFangDaKai] text-center">新增账号</h1>
      <AdminAccountForm />
    </div>
  </dialog>
</template>
