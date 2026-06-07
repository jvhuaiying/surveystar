<script setup lang="ts">
import { useAccountDialogStore } from "@/stores/account-dialog";

const dialogStore = useAccountDialogStore();
</script>

<template>
  <div
    class="p-4 w-full flex flex-row justify-center items-center gap-x-4 bg-slate-200 shadow-md rounded-md"
  >
    <el-input />
    <el-button type="primary">查找</el-button>
    <el-button type="success" class="ml-0!" @click="dialogStore.open"> 新增 </el-button>
  </div>
</template>
