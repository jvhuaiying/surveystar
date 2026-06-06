<script setup lang="ts">
import { useWebsiteInfoStore } from "@/stores/website-info";

const props = defineProps({
  description: Boolean,
});

const websiteInfoStore = useWebsiteInfoStore();
</script>

<template>
  <div class="flex flex-col justify-center items-center gap-y-2">
    <div class="flex flex-row justify-center items-center gap-x-2">
      <img :src="`api/${websiteInfoStore.websiteInfo.logo}`" alt="logo" class="size-7" />
      <h1 class="text-2xl font-[AlimamaDongFangDaKai]">
        {{ websiteInfoStore.websiteInfo.name }}
      </h1>
    </div>
    <span v-if="props.description" class="text-base font-[AlibabaPuHuiTi-3-55] text-gray-600">
      {{ websiteInfoStore.websiteInfo.description }}
    </span>
  </div>
</template>
