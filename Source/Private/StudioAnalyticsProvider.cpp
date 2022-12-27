#include "StudioAnalyticsProvider.h"
#include <Analytics.h>
#include <AnalyticsET.h>
#include <IAnalyticsProviderET.h>
#include <StudioAnalytics.h>

DEFINE_LOG_CATEGORY_STATIC(LogStudioAnalyticsProvider, Display, All);

void FStudioAnalyticsProviderModule::StartupModule()
{
	const FAnalytics::ConfigFromIni AnalyticsConfig;
	const TSharedPtr<IAnalyticsProviderET> Provider = StaticCastSharedPtr<IAnalyticsProviderET>(
		FAnalyticsET::Get().CreateAnalyticsProvider(
			FAnalyticsProviderConfigurationDelegate::CreateRaw(
				&AnalyticsConfig,
				&FAnalytics::ConfigFromIni::GetValue
			)
		)
	);
  
	if (!Provider)
	{
		UE_LOG(LogStudioAnalyticsProvider, Error, TEXT("Failed create AnalyticsProviderET for StudioAnalyticsProvider. Ensure required config values are set."));
		return;
	}
  
	Provider->StartSession();
	Provider->SetUserID(FString(FPlatformProcess::UserName(false)));
	Provider->SetDefaultEventAttributes(
		MakeAnalyticsEventAttributeArray(
			TEXT("ComputerName"), FString(FPlatformProcess::ComputerName()),
			TEXT("ProjectName"), FString(FApp::GetProjectName()),
			TEXT("P4Branch"), FApp::GetBranchName()
		)
	);
	
	FStudioAnalytics::SetProvider(Provider.ToSharedRef());
}
	
IMPLEMENT_MODULE(FStudioAnalyticsProviderModule, StudioAnalyticsProvider)