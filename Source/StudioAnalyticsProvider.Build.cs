using UnrealBuildTool;

public class StudioAnalyticsProvider : ModuleRules
{
	public StudioAnalyticsProvider(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = ModuleRules.PCHUsageMode.UseExplicitOrSharedPCHs;
		bEnforceIWYU = true;
		
		PrivateDependencyModuleNames.AddRange(
			new string[]
			{
				"Core",
				"Engine",
				"Analytics",
				"AnalyticsET",
			}
		);
	}
}