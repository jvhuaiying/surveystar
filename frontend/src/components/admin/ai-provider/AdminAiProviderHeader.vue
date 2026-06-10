<script setup lang="ts">
import { useAiProviderDialogStore } from "@/stores/ai-provider-dialog";

const dialogStore = useAiProviderDialogStore();
</script>

<template>
  <div
    class="p-4 w-full flex flex-row justify-center items-center gap-x-4 bg-slate-200 shadow-md rounded-md"
  >
    <el-input />
    <el-button type="primary">查找</el-button>
    <el-button type="success" class="ml-0!" @click="dialogStore.open('create', null)"> 新增 </el-button>
  </div>
</template>
