<script setup lang="ts">
import { useAiProviderDialogStore } from "@/stores/ai-provider-dialog";
import AdminAiProviderEditForm from "@/components/admin/ai-provider/AdminAiProviderEditForm.vue";
import AdminAiProviderForm from "@/components/admin/ai-provider/AdminAiProviderForm.vue";

const dialogStore = useAiProviderDialogStore();

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
      {{ dialogStore.mode === "create" ? "新增供应商" : "编辑供应商" }}
    </h1>
    <AdminAiProviderForm model="dialog" v-show="dialogStore.mode === 'create'" />
    <AdminAiProviderEditForm v-show="dialogStore.mode === 'edit'" />
  </el-dialog>
</template>
