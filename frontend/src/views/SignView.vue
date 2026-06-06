<script setup lang="ts">
import { useElementSize } from "@vueuse/core";
import LogoTitlePart from "@/components/LogoTitlePart.vue";
import { onMounted, ref, useTemplateRef, watch } from "vue";

const el = useTemplateRef("el");
const { width, height } = useElementSize(el);

const background_url = ref("");

const get_background_url = () => {
  background_url.value = `https://picsum.photos/${width.value}/${height.value}`;
};

onMounted(() => {
  get_background_url();
});

watch([width, height], () => {
  get_background_url();
});
</script>

<template>
  <div
    ref="el"
    :style="{ backgroundImage: `url(${background_url})` }"
    class="w-full h-screen flex flex-row justify-center items-center"
  >
    <div class="p-6 w-96 bg-white rounded-lg shadow-md border border-gray-200">
      <div class="flex flex-col justify-center items-center gap-y-6">
        <LogoTitlePart :description="true" />
        <RouterView />
      </div>
    </div>
  </div>
</template>
