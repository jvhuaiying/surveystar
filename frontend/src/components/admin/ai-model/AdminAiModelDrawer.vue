<script setup lang="ts">
import { useAiModelDrawerStore } from "@/stores/ai-model-drawer";
import AdminAiProviderForm from "../ai-provider/AdminAiProviderForm.vue";

const drawerStore = useAiModelDrawerStore();
</script>

<template>
  <el-drawer
    v-model="drawerStore.visible"
    direction="rtl"
    :show-close="false"
    size="420"
    destroy-on-close
  >
    <div class="p-6 flex flex-col justify-center items-center gap-y-4">
      <h1 class="text-2xl font-[AlimamaDongFangDaKai] text-center">大模型提供商管理</h1>
      <AdminAiProviderForm model="drawer" />
    </div>
  </el-drawer>
</template>
