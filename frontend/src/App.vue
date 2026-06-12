<script setup lang="ts">
import { watch } from "vue";
import { RouterView } from "vue-router";
import { ElConfigProvider } from "element-plus";
import zhCn from "element-plus/es/locale/lang/zh-cn";
import { getWebsiteInfoUtils } from "@/utils/admin/website-info";

const { data, isLoading, error } = getWebsiteInfoUtils();

watch(data, (data) => {
  if (!data) return;

  document.querySelector("title")?.remove();
  document.querySelector("link[rel='icon']")?.remove();

  const title = document.createElement("title");
  title.textContent = data.name;
  document.head.appendChild(title);

  const link = document.createElement("link");
  link.rel = "icon";
  link.href = `/api/${data.logo}`;
  document.head.appendChild(link);
});

watch(error, (err) => {
  if (err) ElMessage({ message: err.message, type: "error" });
});
</script>

<template>
  <el-config-provider :locale="zhCn">
    <RouterView v-loading.fullscreen.lock="isLoading" />
  </el-config-provider>
</template>
