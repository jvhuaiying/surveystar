<script setup lang="ts">
import { watch } from "vue";
import { RouterView } from "vue-router";
import { useQuery } from "@pinia/colada";
import { ElConfigProvider } from "element-plus";
import { getWebsiteInfo } from "@/api/website-info";
import zhCn from "element-plus/es/locale/lang/zh-cn";

const { data, isLoading, error } = useQuery({
  key: ["websiteInfo"],
  query: getWebsiteInfo,
});

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
    <RouterView v-loading="isLoading" />
  </el-config-provider>
</template>
