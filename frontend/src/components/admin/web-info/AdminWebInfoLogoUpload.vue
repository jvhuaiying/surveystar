<script setup lang="ts">
import { computed, useTemplateRef } from "vue";
import { updateWebsiteLogo } from "@/api/website-info";
import { useMutation, useQueryCache } from "@pinia/colada";
import type { MessageResponseSchemas } from "@/types/account";
import { getWebsiteInfoUtils } from "@/utils/admin/website-info";

const queryCache = useQueryCache();
const ref0 = useTemplateRef("ref0");
const { data } = getWebsiteInfoUtils();
const props = defineProps<{ height: number }>();

const imageUrl = computed(() => {
  return data.value?.logo ? `/api/${data.value.logo}` : "";
});

const { mutate, isLoading } = useMutation({
  key: ["update-website-logo"],
  mutation: (data: File) => updateWebsiteLogo(data),
  onSuccess: (data: MessageResponseSchemas) => {
    ElMessage({ message: data.detail, type: "success" });
  },
  onError: (err: Error) => {
    ElMessage({ message: err.message, type: "error" });
  },
  onSettled: () => queryCache.invalidateQueries({ key: ["websiteInfo"] }),
});

const fun0 = () => {
  ref0.value?.click();
};

const fun1 = (event: Event) => {
  const target = event.target as HTMLInputElement;
  if (target.files && target.files[0]) {
    mutate(target.files[0]);
  }
};
</script>

<template>
  <input type="file" name="logo" class="hidden" ref="ref0" @change="fun1" />
  <img
    :src="imageUrl"
    class="cursor-pointer"
    v-loading="isLoading"
    :style="{ height: props.height + 'px' }"
    @click="fun0"
  />
</template>
