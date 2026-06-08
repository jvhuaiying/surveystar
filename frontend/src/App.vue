<script setup lang="ts">
import { watch } from "vue";
import { RouterView } from "vue-router";
import { useQuery } from "@pinia/colada";
import { useHead } from "@unhead/vue";
import { ElConfigProvider } from "element-plus";
import { getWebsiteInfo } from "@/api/website-info";
import zhCn from "element-plus/es/locale/lang/zh-cn";

const { data, isLoading, error } = useQuery({
  key: ["websiteInfo"],
  query: getWebsiteInfo,
});

useHead({
  title: () => data.value?.name ?? "",
  link: () => (data.value?.logo ? [{ rel: "icon", href: `api/${data.value.logo}` }] : []),
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
