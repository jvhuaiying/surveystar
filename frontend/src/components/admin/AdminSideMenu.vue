<script setup lang="ts">
import { User } from "@element-plus/icons-vue";
</script>

<template>
  <el-menu default-active="2" class="el-menu-vertical-demo" :collapse="false">
    <el-menu-item index="1">
      <el-icon><User /></el-icon>
      <template #title>账号管理</template>
    </el-menu-item>
  </el-menu>
</template>
