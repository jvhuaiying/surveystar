<script setup lang="ts">
import { useQueryCache } from "@pinia/colada";
import type { WebsiteInfoResponseSchemas } from "@/types/website-info";

const props = defineProps({
  description: Boolean,
});

const queryCache = useQueryCache();
const entry = queryCache.get<WebsiteInfoResponseSchemas>(["websiteInfo"]);
</script>

<template>
  <div class="flex flex-col justify-center items-center gap-y-2">
    <div class="flex flex-row justify-center items-center gap-x-2">
      <el-image :src="`/api/${entry?.state.value.data?.logo}`" alt="logo" class="size-7" />
      <h1 class="text-2xl font-[AlimamaDongFangDaKai]">
        {{ entry?.state.value.data?.name }}
      </h1>
    </div>
    <span v-if="props.description" class="text-base font-[AlibabaPuHuiTi-3-55] text-gray-600">
      {{ entry?.state.value.data?.description }}
    </span>
  </div>
</template>
