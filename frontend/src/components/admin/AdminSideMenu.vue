<script setup lang="ts">
import { Connection, Cpu, DataLine, Monitor, User } from "@element-plus/icons-vue";
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
    <el-sub-menu index="2">
      <template #title>
        <el-icon><Cpu /></el-icon>
        <span>模型管理</span>
      </template>
      <el-menu-item index="/admin/ai-provider">
        <el-icon><Connection /></el-icon>
        <template #title>提供商管理</template>
      </el-menu-item>
      <el-menu-item index="/admin/ai-model">
        <el-icon><DataLine /></el-icon>
        <template #title>大模型管理</template>
      </el-menu-item>
    </el-sub-menu>
  </el-menu>
</template>

<style scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
}
</style>
