export type WebsiteInfoResponseSchemas = {
  id: string;
  logo: string;
  name: string;
  description: string;
  icp: string | null;
};

export type UpdateWebsiteInfoRequestSchemas = {
  name: string;
  description: string;
  icp: string | null;
};
