<script setup lang="ts">
import { useTemplateRef } from "vue";
import { useElementSize } from "@vueuse/core";
import { useAiModelDrawerStore } from "@/stores/ai-model-drawer";
import AdminAiProviderForm from "../ai-provider/AdminAiProviderForm.vue";

const el = useTemplateRef("el");
const { width } = useElementSize(el);
const drawerStore = useAiModelDrawerStore();
</script>

<template>
  <el-drawer
    v-model="drawerStore.visible"
    direction="rtl"
    :show-close="false"
    body-class="w-96"
    :size="width || '50%'"
    destroy-on-close
  >
    <div ref="el">
      <div class="p-6 flex flex-col justify-center items-center gap-y-4">
        <h1 class="text-2xl font-[AlimamaDongFangDaKai] text-center">大模型提供商管理</h1>
        <AdminAiProviderForm model="drawer" />
      </div>
    </div>
  </el-drawer>
</template>
