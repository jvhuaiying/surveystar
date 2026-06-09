<script setup lang="ts">
import { User, Monitor } from "@element-plus/icons-vue";
</script>

<template>
  <el-menu default-active="/admin" class="el-menu-vertical-demo h-full" :collapse="false" router>
    <el-menu-item index="/admin">
      <el-icon><Monitor /></el-icon>
      <template #title>网站信息</template>
    </el-menu-item>
    <el-menu-item index="/admin/account">
      <el-icon><User /></el-icon>
      <template #title>账号管理</template>
    </el-menu-item>
  </el-menu>
</template>

<style scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
}
</style>
