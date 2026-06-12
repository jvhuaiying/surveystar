<script setup lang="ts">
import { getWebsiteInfoUtils } from "@/utils/admin/website-info";

const props = defineProps({
  description: Boolean,
});

const { data } = getWebsiteInfoUtils();
</script>

<template>
  <div class="flex flex-col justify-center items-center gap-y-2">
    <div class="flex flex-row justify-center items-center gap-x-2">
      <el-image :src="`/api/${data?.logo}`" alt="logo" class="size-7" />
      <h1 class="text-2xl font-[AlimamaDongFangDaKai]">
        {{ data?.name }}
      </h1>
    </div>
    <span v-if="props.description" class="text-base font-[AlibabaPuHuiTi-3-55] text-gray-600">
      {{ data?.description }}
    </span>
  </div>
</template>
