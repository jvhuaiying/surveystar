<script setup lang="ts">
import { onMounted } from "vue";
import { RouterView } from "vue-router";
import { ElConfigProvider } from "element-plus";
import { getWebsiteInfo } from "@/api/website-info";
import zhCn from "element-plus/es/locale/lang/zh-cn";
import { useWebsiteInfoStore } from "@/stores/website-info";

const websiteInfoStore = useWebsiteInfoStore();
onMounted(() => {
  getWebsiteInfo()
    .then((res) => {
      websiteInfoStore.setWebsiteInfo(res);
      const titleEl = document.createElement("title");
      titleEl.textContent = websiteInfoStore.websiteInfo.name;
      document.head.appendChild(titleEl);
      const link = document.createElement("link");
      link.rel = "icon";
      link.href = `api/${websiteInfoStore.websiteInfo.logo}`;
      document.head.appendChild(link);
    })
    .catch((err: Error) => {
      ElMessage({
        message: err.message,
        type: "error",
      });
    });
});
</script>

<template>
  <el-config-provider :locale="zhCn">
    <RouterView />
  </el-config-provider>
</template>
