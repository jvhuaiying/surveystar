<script setup lang="ts">
import { usePromptDialogStore } from "@/stores/prompt-dialog";
import AdminPromptForm from "@/components/admin/prompt/AdminPromptForm.vue";

const dialogStore = usePromptDialogStore();

const handleClose = () => {
  dialogStore.close();
};
</script>

<template>
  <el-dialog
    v-model="dialogStore.visible"
    :before-close="handleClose"
    :show-close="false"
    header-class="p-0!"
    width="420"
    align-center
    destroy-on-close
    body-class="p-6 flex flex-col justify-center items-center gap-y-4"
  >
    <h1 class="text-2xl font-[AlimamaDongFangDaKai] text-center">
      {{ dialogStore.mode === "create" ? "新增系统提示词" : "编辑系统提示词" }}
    </h1>
    <AdminPromptForm />
  </el-dialog>
</template>
