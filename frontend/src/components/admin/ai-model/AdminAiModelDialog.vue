<script setup lang="ts">
import { useAiModelDialogStore } from "@/stores/ai-model-dialog";
import AdminAiModelEditForm from "@/components/admin/ai-model/AdminAiModelEditForm.vue";
import AdminAiModelForm from "@/components/admin/ai-model/AdminAiModelForm.vue";

const dialogStore = useAiModelDialogStore();

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
      {{ dialogStore.mode === "create" ? "新增大模型" : "编辑大模型" }}
    </h1>
    <AdminAiModelForm v-show="dialogStore.mode === 'create'" />
    <AdminAiModelEditForm v-show="dialogStore.mode === 'edit'" />
  </el-dialog>
</template>
