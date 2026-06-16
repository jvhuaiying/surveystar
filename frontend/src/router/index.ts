import { useAccountStore } from "@/stores/account";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/sign",
      name: "signPage",
      component: () => import("@/views/SignView.vue"),
      children: [
        {
          path: "",
          name: "signIn",
          component: () => import("@/components/sign/SignInForm.vue"),
        },
      ],
    },
    {
      path: "/admin",
      name: "adminHome",
      component: () => import("@/views/admin/AdminHomeView.vue"),
      children: [
        {
          path: "",
          name: "adminWebInfo",
          component: () => import("@/views/admin/AdminWebInfo.vue"),
        },
        {
          path: "account",
          name: "adminAccount",
          component: () => import("@/views/admin/AdminAccountView.vue"),
        },
        {
          path: "ai-provider",
          name: "adminAiProvider",
          component: () => import("@/views/admin/AdminAiProviderView.vue"),
        },
        {
          path: "ai-model",
          name: "adminAiModel",
          component: () => import("@/views/admin/AdminAiModelView.vue"),
        },
        {
          path: "prompt",
          name: "adminPrompt",
          component: () => import("@/views/admin/AdminPromptView.vue"),
        },
      ],
    },
  ],
});

router.beforeEach((to) => {
  const accountStore = useAccountStore();

  if (!accountStore.access_token && to.name !== "signIn") {
    return { name: "signIn" };
  }

  if (accountStore.access_token && to.name === "signIn") {
    switch (accountStore.kind) {
      case "admin":
        return { name: "adminWebInfo" };
    }
  }
});

export default router;
