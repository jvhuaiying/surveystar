<script setup lang="ts">
import AdminWebInfoForm from "@/components/admin/web-info/AdminWebInfoForm.vue";
import AdminWebInfoLogoUpload from "@/components/admin/web-info/AdminWebInfoLogoUpload.vue";
import { useElementSize } from "@vueuse/core";
import { useTemplateRef } from "vue";

const el = useTemplateRef("el");
const { height } = useElementSize(el);
</script>

<template>
  <div class="p-6 flex-1 h-full flex flex-row justify-center items-center bg-slate-50">
    <div class="p-6 flex flex-row justify-center items-start gap-x-6 bg-white rounded-lg shadow-lg">
      <div class="flex flex-col justify-center items-center gap-y-6">
        <h1 class="text-2xl font-[AlimamaDongFangDaKai]">网站信息</h1>
        <AdminWebInfoForm ref="el" />
      </div>
      <div class="flex flex-col justify-center items-center gap-y-6">
        <h1 class="text-2xl font-[AlimamaDongFangDaKai]">LOGO</h1>
        <AdminWebInfoLogoUpload :height="height" />
      </div>
    </div>
  </div>
</template>
