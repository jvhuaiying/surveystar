<script setup lang="ts">
import { useTemplateRef } from "vue";
import { useElementSize } from "@vueuse/core";
import { useAiModelDialogStore } from "@/stores/ai-model-dialog";
import AdminAiModelForm from "@/components/admin/ai-model/AdminAiModelForm.vue";

const el = useTemplateRef("el");
const { width } = useElementSize(el);
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
    body-class="w-96"
    :width="width"
    align-center
    destroy-on-close
  >
    <div ref="el">
      <div class="p-6 flex flex-col justify-center items-center gap-y-4">
        <h1 class="text-2xl font-[AlimamaDongFangDaKai] text-center">
          {{ dialogStore.mode === "create" ? "新增大模型" : "编辑大模型" }}
        </h1>
        <AdminAiModelForm v-show="dialogStore.mode === 'create'" />
      </div>
    </div>
  </el-dialog>
</template>
