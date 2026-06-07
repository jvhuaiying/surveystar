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
          name: "adminAccount",
          component: () => import("@/views/admin/AdminAccountView.vue"),
        },
      ],
    },
  ],
});

export default router;
